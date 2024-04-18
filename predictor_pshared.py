#código de simluador para un predictor p-shared.
"""
predictor p-shared: utiliza historia local. Donde tenemos una tabla con varios registros de historia. Además, mediante
el PC del branch se indexa una tabla que contiene un registro deslizante con la historia de los saltos que han ocurrido
para branches con un PC que terminan en los índices 00, 01, 10, 11.
"""

class PSharePredictor:
    def __init__(self, p_bits, history_bits):
        self.p_bits = p_bits
        self.history_bits = history_bits
        self.bht = [0] * (2 ** history_bits) #historia de branches
        self.pht = [0] * (2 ** p_bits) #historia de patrones
        self.global_history = 0
    
    def predict(self, pc):
        pht_index = self.global_history % len(self.pht)
        p_prediction = self.pht[pht_index] >> (self.p_bits - 1)
        bht_index = pc % len(self.bht)
        b_prediction = self.bht[bht_index] >> (self.history_bits - 1)
        return p_prediction if p_prediction == b_prediction else 2 #contador de 2 bits

    def update(self, pc, actual_result):
        bht_index = pc % len(self.bht)
        pht_index = self.global_history % len(self.pht)

        if outcome == 1 or outcome == 3: #corregir
            self.bht[bht_index] = min(self.bht[bht_index] + 1,3)
            self.pht[pht_index] = min(self.pht[pht_index] + 1, 2 ** self.p_bits)
        else:
            self.bht[bht_index] = max(self.bht[bht_index] - 1,0)
            self.pht[pht_index] = max(self.pht[pht_index] - 1,0)
        
        self.global_history = ((self.global_history << 1) | outcome) & ((2 ** self.history_bits) - 1)
