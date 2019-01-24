include = True
exclude = False
yes = True
no = False

############ USER DEFINED VARIABLES START ############

# The directory containing the autodlcheck scripts
folder_path = "/home/user/scripts"

# no to disable
enable_disk_check = yes

###### DISK CHECK SECTION - IGNORE IF DISABLED ######

host = "scgi://127.0.0.1:5000"

# The minimum amount of free space (in Gigabytes) to maintain
minimum_space = 5

# GENERAL RULES START

# All minimum requirements must be met by a torrent to be deleted

# Filesize in Gigabytes / Age in Days

minimum_filesize = 5
minimum_age = 7
minimum_ratio = 1.2

# Only the age of a torrent must be higher or equal to this number to be deleted (filesize requirement remains) - no to disable
fallback_age = no

# Only the ratio of a torrent must be higher or equal to this number to be deleted (filesize requirement remains) - no to disable
fallback_ratio = 1.1

# GENERAL RULES END


# Tracker Rules will override general rules - Fill to enable

# include: use general rules | exclude: exclude tracker

# Value Order: 1. Minimum Filesize (GB) 2. Minimum Age 3. Minimum Ratio 4. Fallback Age 5. Fallback Ratio

trackers = {
#                     "demonoid.pw" : [include],
#                     "hdme.eu" : [exclude],
#                     "redacted.ch" : [1, 7, 1.2, no, no],
#                     "hd-torrents.org" : [3, 5, 1.3, 9, 1.3],
#                     "privatehd.to" : [5, 6, 1.2, 12, no],
#                     "apollo.rip" : [2, 5, 1.4, no, 1.8],
           }

# Only delete torrents from trackers with a tracker rule (yes/no)
trackers_only = yes


# Label Rules will override general/tracker rules - Fill to enable

# include: use general/tracker rules | exclude: exclude label

# Value Order: 1. Minimum Filesize (GB) 2. Minimum Age 3. Minimum Ratio 4. Fallback Age 5. Fallback Ratio

labels = {
#                     "Trash" : [include],
#                     "TV" : [exclude],
#                     "HD" : [1, 5, 1.2, 15, 1.2],
         }

# Only delete torrents with labels that have a label rule (yes/no)
labels_only = no

# Exclude torrents without labels (yes/no)
exclude_unlabelled = no


###### IMDB SECTION - IGNORE IF UNWANTED ######

# The IMDB function will only execute if the torrent is attached to a label with an IMDB rule

# Value Order: 1. Minimum IMDB Rating 2. Minimum Votes 3. Skip Foreign Movies (yes/no)

imdb = {
#                     "Hollywood Blockbusters" : [7, 80000, yes],
#                     "Bollywood Classics" : [8, 60000, no],
       }

############ USER DEFINED VARIABLES END ############