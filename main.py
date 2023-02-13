import psycopg2
import time
import matplotlib.pyplot as plt

# Connect to the database
conn = psycopg2.connect(
    host="localhost", database="testdb", user="postgres", password="secretpassword"
)

# Create a cursor
cur = conn.cursor()
cur.execute("CREATE TABLE hello(id int)")

start_time = time.time()

# Execute a query to insert data into the database
for i in range(100000):
    cur.execute("INSERT INTO hello VALUES (%s)", (i,))

# Commit the transactions
conn.commit()

end_time = time.time()

# Calculate the TPS
tps = 100000 / (end_time - start_time)

print("TPS:", tps)

# Create a cursor
cur = conn.cursor()
# Drop the table
cur.execute("DROP TABLE hello")
# Commit the changes
conn.commit()

# Plot the TPS in a graph
plt.plot([tps])
plt.xlabel("Iteration")
plt.ylabel("TPS")
plt.title("TPS Plot")
plt.show()

# Close the cursor and connection
cur.close()
conn.close()
