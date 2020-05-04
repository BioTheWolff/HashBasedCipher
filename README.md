# HashBasedCipher
A small cipher library made in python really quickly

Cipher working with a pair: key and message. The key is required

It is made with SHA-1. Made to be quick rather than totally secure, it only changes letters and figures for now.

I'm planning on trying to find new ways to make it more secure, or less "readable" (especially since the spaces are not
enciphered, you could get something like `UG WHKS4, 4LN0YR0S`!)

## Process
Since everything gets random with hashes and I don't make this to be of a NASA-level security, I can explain everything.
So, let's break down the process.

Concerning the HashBasedGeneration class:

1. We get a SHA-1 hash from the key
2. We generate an ordered list (a-zA-Z0-9) [let's call it `ordered` from now on]
3. We generate a random number times 60 [which I will call `weight`], for each char in the hash. To be able to decipher the message, we seed
the pseudo-random generator with the concerned char.
4. We take the `ordered` and shift it right `round(weight)` times for each char of the hash
5. After storing the whole list of seeded-ly shifted `ordered`s (`shifted lists`), we return them.

Now, for the Encipher and Decipher classes, it is basically the same thing (yes yes, exactly the same code except one line)

1. We take the returned list of `shifted lists`
2. Then make a dict out of each list (the only difference in code is here):
    - Encipher: `ordered` in key and `shifted` in value (`ordered => shifted`)
    - Decipher: `shifted` in key and `ordered` in value (`shifted => ordered`)
3. We calculate where to start in the dicts list (`dl`) using `len(key) % len(dl)`
4. Now, for each element, we (de)cipher it using the dicts list. We will cycle through the `dl` (going back to first element
upon reaching the last), which means depending on the message length, we might not use the full `dl`, or use it fully
more than once.

## How to use

It's really *that* simple!

just import the class you'd want to use (`from HashBasedCipher.encipher import Encipher` or 
`from HashBasedCipher.decipher import Decipher`),
then use `process()` on the class instance you created!

For later referencing, you can always access the message, whether it is enciphered or deciphered, by using the
`message` property of the instance (which will return `None` if no process has already been done)