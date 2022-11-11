import csv
import hashlib
import os

DATA_FOLDER_PATH = os.path.join(os.getcwd(), 'data')
USERDATA_FOLDER_PATH = os.path.join(DATA_FOLDER_PATH, 'USERDATA')
REGISTERED_USERS_FILE_PATH = os.path.join(DATA_FOLDER_PATH, 'registered_users.csv')
CSV_HEADERS = ['uname', 'pwd_hash', 'data_subfolderpath']


def hash_sha256(plaintext: str):
    return hashlib.sha256(plaintext.encode()).hexdigest()


def __check_paths():
    if not os.path.exists(DATA_FOLDER_PATH):
        os.mkdir(DATA_FOLDER_PATH)
        os.mkdir(USERDATA_FOLDER_PATH)

    if not os.path.isfile(REGISTERED_USERS_FILE_PATH): # if registered users file 404
        with open(REGISTERED_USERS_FILE_PATH, 'w', encoding='utf-8') as fp:
            template_writer = csv.writer(fp)
            template_writer.writerow(CSV_HEADERS) # write default headers


def __create_new_user_record(hashed_login_info: tuple[str], plaintext_uname: str, fieldnames: dict[str, list]):
    os.mkdir(os.path.join(USERDATA_FOLDER_PATH, f'{plaintext_uname}')) # create userdata folder for new user

    with open(REGISTERED_USERS_FILE_PATH, 'a', encoding='utf-8') as users_csv:
        writer = csv.DictWriter(users_csv, fieldnames=fieldnames.keys())
 
        user_info = {
            'uname': hashed_login_info[0],
            'pwd_hash': hashed_login_info[1],
            'data_subfolderpath': os.path.join(USERDATA_FOLDER_PATH, f'{plaintext_uname}')
        }
        writer.writerow(user_info) # enter new record


def __get_csv_as_dict():
    columns = {}
    for i in CSV_HEADERS:
        columns[i] = []

    with open(REGISTERED_USERS_FILE_PATH, 'r', encoding='utf-8') as users_csv:
        reader = csv.DictReader(users_csv)

        for row in reader: # {col1: val1, col2: val2, ...}
            for k, v in row.items():
                columns.get(k).append(v) # expected each value in k-v pair to be type list
    
    return columns


def signup(new_uname: str, new_pwd: str):
    __check_paths()
    
    # hash username and password with SHA-256
    uname = new_uname
    pwd_hash = hash_sha256(new_pwd)

    # append each val in column to list
    columns = __get_csv_as_dict()    

    # Check if existing user
    if uname in columns.get('uname'):
        return False
    
    # Create a new record
    __create_new_user_record(hashed_login_info=(uname, pwd_hash), plaintext_uname=new_uname, fieldnames=columns)
    return True


def login(uname: str, pwd_hash: str):
    # check if uname exists
    records = __get_csv_as_dict() # Entire csv file as a dictionary
    if uname not in records.get('uname'): # User does not exist
        return False, None

    # get exact row matching given uname
    record_idx = records.get('uname').index(uname) # index of row containing given username
    with open(REGISTERED_USERS_FILE_PATH, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for idx, row in enumerate(reader):
            if idx == record_idx:
                record = row

    # login
    if record.get('pwd_hash') == pwd_hash: # compare password hashes
        return True, [record.get('uname'), record.get('data_subfolderpath')] # SUCCESS, [username, datapath]
    
    return False, None


# TESTING ONLY
# The test case I've run below is not very well written, there will be a much better implementation in 
# the actual driver.py file

if __name__ == '__main__':
    print('Signup')
    u = input('Enter uname: ')
    p = input('Enter password: ')
    res = signup(u, p)
    if not res:
        print('Existing user')

    print('Login')
    u1 = input('Enter username: ')
    p1 = input('Enter password: ')
    res1, data = login(u1, hash_sha256(p1))
    if not res1:
        print('Invalid username or pwd')
    else:
        print(f'Welcome {data[0]}\nYour data folder is at {data[1]}')