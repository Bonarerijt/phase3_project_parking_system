from database.db import init_db, get_session

def main():
    init_db()
    session = get_session()
    

if __name__ == "__main__":
    main()
