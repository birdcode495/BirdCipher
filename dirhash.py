from checksumdir import dirhash

directory  = 'C:/BirdCipher/Sources'
md5hash    = dirhash(directory, 'md5')
sha1hash   = dirhash(directory, 'sha1')
sha256hash = dirhash(directory, 'sha256')

print(sha256hash)