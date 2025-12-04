from database.db import init_db
from cli import ParkingCLI



if __name__ == "__main__":
    init_db()
    ParkingCLI.start()
