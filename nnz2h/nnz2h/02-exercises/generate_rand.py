import random

# Base sequences to sample/mutate from
templates = [
    "dwwweaasssas........ddddwwwwddweassssaas...........dd.ssseassaase......aaasssssss.wds..........asssseadwwwwwe.........aaddddddddadwwwesssdddddswwddd........w..s..wwwww.we",
    "dwwweaassssee.....dddwwwedwweasssds...........daadssssedaasseaaaa......ssssssdaaas.....addsssasedwwww...a......aasssewwwdwwwwwwe",
    "dwwwesssdddwww..........aadwwwwessss.........sssseaass.......aaassssssas.......assssedddwwwedddsss...........dssssssse"
]

chars = ['a', 's', 'd', 'w', '.', 'e']

def mutate_sequence(seq, mutation_rate=0.01):
    seq_list = list(seq)
    for i in range(len(seq_list)):
        if random.random() < mutation_rate:
            seq_list[i] = random.choice(chars)
    return "".join(seq_list)

# Generate 5,000 lines and write to output file
with open("sequences_5000.txt", "w") as f:
    for _ in range(5000):
        base_seq = random.choice(templates)
        seq = mutate_sequence(base_seq, mutation_rate=0.005) # Adjust or set to 0 for exact copies
        score = random.randint(1000, 9999)
        f.write(f"{seq} {score}\n")