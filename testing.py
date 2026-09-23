import hashlib
import time


class Block:
    def __init__(self, index, vote, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.vote = vote
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = (
            str(self.index)
            + str(self.timestamp)
            + str(self.vote)
            + str(self.previous_hash)
        )
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.voters = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, "Genesis", "0"))

    def get_latest_block(self):
        return self.chain[-1]

  def add_vote(self, voter_id, candidate):
    if voter_id in self.voters:
        print("Already Voted!")
        return

    self.voters.add(voter_id)

    block = Block(
        len(self.chain),
        {"voter": voter_id, "candidate": candidate},
        self.get_latest_block().hash
    )

    self.chain.append(block)

    print(f"Vote Successful: {candidate}")
    print("Hash:", block.hash[:10])

    def show_results(self):
        results = {}

        for block in self.chain[1:]:
            candidate = block.vote["candidate"]
            results[candidate] = results.get(candidate, 0) + 1

        print("\nResults:")

        if not results:
            print("No votes yet")
        else:
            for c in results:
                print(c, ":", results[c])

    def show_chain(self):
        print("\nBlockchain:")

        for block in self.chain:
            print("Index:", block.index)
            print("Vote:", block.vote)
            print("Hash:", block.hash)
            print()


bc = Blockchain()

while True:
    print("\n--- Voting System ---")
    print("1 Vote")
    print("2 Results")
    print("3 Blockchain")
    print("4 Exit")

    try:
        choice = int(input("Enter choice (1-4): "))
    except:
        print("Invalid input!")
        continue

    if choice == 1:
        voter = input("Enter Voter ID: ")

        print("1 Alice")
        print("2 Bob")

        try:
            c = int(input("Choose candidate: "))
        except:
            print("Invalid input!")
            continue

        if c == 1:
            bc.add_vote(voter, "Alice")
        elif c == 2:
            bc.add_vote(voter, "Bob")
        else:
            print("Invalid candidate")

    elif choice == 2:
        bc.show_results()

    elif choice == 3:
        bc.show_chain()

    elif choice == 4:
        print("Thank you")
        break