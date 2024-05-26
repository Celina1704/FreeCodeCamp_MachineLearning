from collections import defaultdict

def player(prev_play, opp_hist=[], play_order=defaultdict(int)):
 
    if not isinstance(opp_hist, list):
        opp_hist = []

    prev_play = prev_play or 'R'

    opp_hist.append(prev_play)

    pred = 'S'
    n = 4 

    #update play_order dictionary
    if len(opp_hist) > n:
        seq = "".join(opp_hist[(n-9):])
        play_order[seq] += 1
        
        seq_min1 = "".join(opp_hist[(n-8):])
        if len(seq) == n+1:
            potential_plays = [seq_min1 + "R", seq_min1 + "P", seq_min1 + "S"]
            sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
            if sub_order:
                pred = max(sub_order, key=sub_order.get)[(n-5):]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    return ideal_response[pred]