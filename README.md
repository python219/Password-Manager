# Password-Manager
A very simple password manager with functions to create, add, search, or delete your passwords. It does not encrypt passwords but that feature is planned.

# Usage
Navigate to the file using cmd then use one of the following functions:

### 1. add

  type "add (name of app or website) (password)"

  Entering the password is optional. If you do not enter in the password a password will be randomly generated. The password will then be saved and copied.

  Example: `passwords.py add microsoft pass1234`

  pass1234 would be copied to the clipboard

### 2. search

type "search (name of app or website)"

The program will search for a password added by the "add" function and then copy it to the clipboard.

Example: `passwords.py search microsoft`

pass1234 would be copied to the clipboard

### 3. delete

type "delete (name of app or website)"

The program will search for the password and then delete it from the database.

Example: `passwords.py delete microsoft`

You would no longer be able to find the password using the "search" function.
