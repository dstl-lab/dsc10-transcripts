"""Visualize a histogram of messages sent per student."""

# %%
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set_theme(style="whitegrid")

    conn = duckdb.connect("database.db", read_only=True)

    result = conn.execute("""
        SELECT c.student_email, COUNT(*) as message_count
        FROM message m
        JOIN conversation c ON m.conversation_id = c.id
        WHERE m.role = 'STUDENT'
        GROUP BY c.student_email
    """).fetchall()

    conn.close()

    message_counts = [row[1] for row in result]

    plt.figure(figsize=(10, 6))
    sns.histplot(message_counts, bins=30)
    plt.xlabel("Number of Messages")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Messages Sent per Student")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
