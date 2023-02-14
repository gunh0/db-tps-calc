import psycopg2
import time
import matplotlib.pyplot as plt

# Connect to the database
conn = psycopg2.connect(
    host="localhost", database="testdb", user="postgres", password="secretpassword"
)

# import mysql.connector
# conn = mysql.connector.connect(
#     host="localhost", database="testdb", user="root", password="secretpassword"
# )

# Create a cursor
cur = conn.cursor()

# Array to store the TPS values
tps_values = []
# Array to store the number of transactions
num_transactions = []

# Loop to increase the number of transactions
for i in range(1, 5):
    cur.execute("CREATE TABLE hello(id int)")

    start_time = time.time()

    # Execute a query to insert data into the database
    for j in range(10**i):
        cur.execute("INSERT INTO hello VALUES (%s)", (j,))

    # Commit the transactions
    conn.commit()

    end_time = time.time()

    # Calculate the TPS
    tps = 10**i / (end_time - start_time)
    num_transactions.append(10**i)
    print("Time:", end_time - start_time)
    print("Transactions:", 10**i)
    print("TPS:", tps)
    tps_values.append(tps)

    cur.execute("DROP TABLE hello")
    conn.commit()


# Plot the TPS in a graph
plt.plot(num_transactions, tps_values, "o-")
plt.xlabel("Number of Transactions")
plt.ylabel("TPS")
plt.title("TPS Plot")
# plt.show()

# Save the plot as a PNG image
plt.savefig("tps_plot.png", dpi=300, bbox_inches="tight")

# Close the cursor and connection
cur.close()
conn.close()
