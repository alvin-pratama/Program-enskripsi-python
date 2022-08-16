import hashlib
import zlib

s_data = input("Masukkan kata/kalimat yang akan diEncrypt: ")

print("""
Opsi Encrypt to:
# Secure Hashing
1. md5
2. sha1
3. sha256
4. sha512
# Built-In Hashing
5. hash
# Checksums
6. adler32
7. crc32
	""")

n_secure_hasing = """Secure hashes and message digests have evolved over the years. From MD5 to SHA1 to SHA256 to SHA512.
Each method grows in size, improving security and reducing the risk of hash collisions. A collision is when two different arrays of data resolve to the same hash.
Hashing can take a large amount of arbitrary data and build a digest of the content. Open-source software builds digests of their packages to help users know that they can trust that files haven’t been tampered with. Small changes to the file will result in a much different hash.
Look at how different two MD5 hashes are after changing one character.
"""
n_md5 = """MD5– 16 bytes/128 bit
MD5 hashes are 16 bytes or 128 bits long. See the example below, note that a hex digest is representing each byte as a hex string (i.e. the leading 09 is one byte). MD5 hashes are no longer commonly used.
"""
n_sha1 = """SHA1–20 bytes/160 bit
SHA1 hashes are 20 bytes or 160 bits long. SHA1 hashes are also no longer commonly used.
"""
n_sha256 = """SHA256–32 bytes/256 bit
SHA256 hashes are 32 bytes or 256 bits long. SHA256 hashes are commonly used.
"""
n_sha512 = """SHA512–64 bytes/512 bit
SHA512 hashes are 64 bytes or 512 bits long. SHA512 hashes are commonly used.
"""
n_built_in_hasing = """In Python 2.x, it would be deterministic most of the time but not always. Python 3.x added randomness to .hash() to improve security. The default sort order of dictionaries, sets, and lists is backed by built-in hashing.
"""
n_checksums = """Checksums are used to validate data in a file. ZIP files use checksums to ensure a file is not corrupt when decompressing. Unlike Python’s built-in hashing, it’s deterministic. Alder32 is usually a better choice as it’s much faster and almost as reliable as crc32. For a small database, adler32 could be used as a simple ID hash. But collisions will quickly become a concern as data grows.
"""

opsi = int(input("Masukkan angka opsi: "))

match opsi:
	case 1:
		print("\nNoted: "+n_secure_hasing)
		print(n_md5)
		o_data = hashlib.md5(s_data.encode("utf-8")).hexdigest()
		print("Result of encrypt md5 "+s_data+" adalah: "+o_data)
		print(len(hashlib.md5(s_data.encode("utf-8")).digest()))
	case 2:
		print("\nNoted: "+n_secure_hasing)
		print(n_sha1)
		o_data = hashlib.sha1(s_data.encode('utf-8')).hexdigest()
		print("Result of encrypt sha1 "+s_data+" adalah: "+o_data)
		print(len(hashlib.sha1(s_data.encode("utf-8")).digest()))
	case 3:
		print("\nNoted: "+n_secure_hasing)
		print(n_sha256)
		o_data = hashlib.sha256(s_data.encode('utf-8')).hexdigest()
		print("Result of encrypt sha256 "+s_data+" adalah: "+o_data)
		print(len(hashlib.sha256(s_data.encode("utf-8")).digest()))
	case 4:
		print("\nNoted: "+n_secure_hasing)
		print(n_sha512)
		o_data = hashlib.sha512(s_data.encode('utf-8')).hexdigest()
		print("Result of encrypt sha512 "+s_data+" adalah: "+o_data)
		print(len(hashlib.sha512(s_data.encode("utf-8")).digest()))
	case 5:
		print("\nNoted: "+n_built_in_hasing)
		o_data = hash(s_data.encode('utf-8'))
		print("Result of encrypt hash "+s_data+" adalah: "+str(o_data))
	case 6:
		print("\nNoted: "+n_checksums)
		o_data = zlib.adler32(s_data.encode('utf-8'))
		print("Result of encrypt adler32 "+s_data+" adalah: "+str(o_data))
	case 7:
		print("\nNoted: "+n_checksums)
		o_data = zlib.crc32(s_data.encode('utf-8'))
		print("Result of encrypt crc32 "+s_data+" adalah: "+str(o_data))
	case _:
		c_int = str(opsi)
		print("No option for number "+c_int)