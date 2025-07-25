import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()

student_record = [
    (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
    (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
    (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
]
# Using executemany to insert multiple records
cursor.executemany('''INSERT INTO student_record (Enrollment, name, subject,Mark) 
                      VALUES (?, ?, ?,?)''', student_record)

# Commit the changes
conn.commit()


cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()
# Display the results
print("All Student Records:")
for row in rows:
    print(row)

cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Verify the update
cursor.execute('SELECT name, MArk FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")


# Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' ''')

# Commit the changes
conn.commit()

# Verify the deletion
cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted_name = cursor.fetchone()

if deleted_name is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")


# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: ${avg_mark:.2f}")

# Close the connection
conn.close()
