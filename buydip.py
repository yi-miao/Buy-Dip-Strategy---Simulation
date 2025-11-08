import numpy as np
import matplotlib.pyplot as plt

class BuyDip:
    def __init__(self, start_x=100, start_y=300, drop_angle_deg=-75, rise_angle_deg=45,
                 pullback_percents=(0.1, 0.2, 0.3), num_buys=10):
        self.start_x = start_x
        self.start_y = start_y
        self.drop_angle_rad = np.radians(drop_angle_deg)
        self.rise_angle_rad = np.radians(rise_angle_deg)
        self.pullback_percents = pullback_percents
        self.num_buys = num_buys
        self.colors = ['green', 'gold', 'red']

    def simulate(self):
        plt.figure(figsize=(9, 6))

        for i, perc in enumerate(self.pullback_percents):
            color = self.colors[i]

            # ── Geometry: compute bottom point using angle and pullback depth ──
            dy_drop = self.start_y * perc
            drop_length = dy_drop / abs(np.sin(self.drop_angle_rad))  # hypotenuse
            dx_drop = np.cos(self.drop_angle_rad) * drop_length
            dy_drop = np.sin(self.drop_angle_rad) * drop_length
            turn_x = self.start_x + dx_drop
            turn_y = self.start_y + dy_drop

            # ── Recovery endpoint ──
            dy_rise = self.start_y - turn_y
            dx_rise = dy_rise / np.tan(self.rise_angle_rad)
            end_x = turn_x + dx_rise

            # ── Dip-buying strategy: buy from halfway down to bottom ──
            dip_amount = self.start_y - turn_y
            buy_start = self.start_y - 0.5 * dip_amount
            buy_end = turn_y
            buy_prices = np.linspace(buy_start, buy_end, self.num_buys)

            # ── Fixed shares per buy ──
            shares_bought = np.ones_like(buy_prices)  # 1 share per buy
            total_shares = np.sum(shares_bought)
            total_cost = np.sum(buy_prices)
            avg_cost = total_cost / total_shares

            # ── Breakeven point ──
            breakeven_y = avg_cost
            breakeven_x = turn_x + (breakeven_y - turn_y) / np.tan(self.rise_angle_rad)

            # ── Final value and return ──
            final_price = self.start_y
            final_value = total_shares * final_price
            return_pct = (final_value - total_cost) / total_cost * 100

            # ── Buy point markers ──
            buy_x = self.start_x + (buy_prices - self.start_y) / np.tan(self.drop_angle_rad)

            # ── Plot scenario ──
            label = f'{int(perc*100)}% Pullback'
            plt.plot([self.start_x, turn_x], [self.start_y, turn_y], color='blue', linestyle='-', label=label)
            plt.plot([turn_x, end_x], [turn_y, self.start_y], color=color, linestyle='-')

            # ── Mark first and last buy ──
            plt.plot(buy_x[0], buy_prices[0], 'o', color=color)
            plt.text(buy_x[0] - 16, buy_prices[0], f'1st Buy\n${int(buy_prices[0])}', color=color, ha='center')

            # ── Mark bottom ──
            plt.plot(turn_x, turn_y, 'x', color=color, markersize=8)
            plt.text(turn_x, turn_y - 10, f'Bottom\n${int(turn_y)}', color=color, ha='center')

            # ── Breakeven ──
            plt.axhline(breakeven_y, color=color, linestyle='--', alpha=0.3)
            plt.plot(breakeven_x, breakeven_y, 's', color=color)
            plt.text(breakeven_x + 8, breakeven_y, f'Breakeven\n${int(breakeven_y)}', color=color, ha='left', va='center')

            # ── Final value ──
            plt.plot(end_x, final_price, 'D', color=color)
            plt.text(end_x, final_price + 4, f'Final\n${int(final_value)}', color=color, ha='center')

            # ── Return annotation ──
            plt.text(end_x + 8, final_price, f'Return\n{return_pct:.1f}%', color=color, ha='left', va='center')

        # ── Final plot setup ──
        plt.title('BuyDip Strategy - Fixed Shares Per Buy')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.xlim(self.start_x - 50, self.start_x + 300)
        plt.ylim(200, 320)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    strategy = BuyDip()
    strategy.simulate()