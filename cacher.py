import os
import time
import logging
from remote_caller import SCGIRequest

try:
	from importlib import reload
except:
	from imp import reload

try:
	import config as cfg
except Exception as e:
	logging.critical("cacher.py: Config Error: Setting cache_interval to default value of 300:", e)


class Cache(SCGIRequest):

	def __init__(self):
		super(Cache, self).__init__()
		self.pendingDeletions, self.torrentsDownloading, self.mountPoints = {}, {}, {}
		self.deletions, self.pending = [], []
		self.torrents = None
		self.lock = False

	def removeTorrent(self, torrentInfo):

		try:
			torrentHash = torrentInfo[2]
			self.torrents.remove(self.torrentsDic[torrentHash])
		except:
			return

	def getTorrents(self):

		while True:

			while self.lock or self.deletions or self.pending:
				time.sleep(60)

			try:
				torrents = self.send(
					"d.multicall2",
					('',
					"complete",
					"d.timestamp.finished=",
					"d.custom1=",
					"t.multicall=,t.url=",
					"d.ratio=",
					"d.size_bytes=",
					"d.name=",
					"d.hash=",
					"d.directory=") )
			except:
				time.sleep(60)
				continue

			torrents.sort()
			[item.append(item[7].rsplit('/', 1)[0] if item[5] in item[7] else item[7]) for item in torrents]
			self.torrents = torrents
			self.torrentsDic = {x[6]:x for x in self.torrents}
			downloading = [tHash[0] for tHash in self.send("d.multicall2", ('', "leeching", "d.hash=") )]
			[tHashes.remove(tHash) for tHashes in self.torrentsDownloading.values() for tHash in tHashes[:] if tHash not in downloading]

			try:
				reload(cfg)
				interval = cfg.cache_interval
			except Exception as e:
				logging.critical("cacher.py: Config Error: Setting cache_interval to default value of 300:", e)
				interval = 300

			time.sleep(interval)

	def getMountPoints(self):

		while not self.torrents:
			time.sleep(1)

		for item in self.torrents:
			parentDirectory = item[8]
			mountPoint = [path for path in [parentDirectory.rsplit('/', num)[0] for num in range(parentDirectory.count('/') )] if os.path.ismount(path)]
			mountPoint = mountPoint[0] if mountPoint else '/'
			self.mountPoints[parentDirectory] = mountPoint
