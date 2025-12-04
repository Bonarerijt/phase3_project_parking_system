from database.db import init_db, get_session

def main():
    init_db()
    session = get_session()
    

if __name__ == "__main__":
    main()

DB_NAME = "parking.db"
RATE = 5
MAX_SLOTS = 10

GROUP_A_SLOTS = ["A1", "A2", "A3", "A4", "A5"]
GROUP_B_SLOTS = ["B1", "B2", "B3", "B4", "B5"]

ALL_SLOTS = GROUP_A_SLOTS + GROUP_B_SLOTS