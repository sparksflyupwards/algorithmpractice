

#include <iostream>

bool * calc_change(unsigned int value, unsigned int k, unsigned int* coins, unsigned int n);

int main()
{
	unsigned int k, n;
	std::cin >> n >> k;
	unsigned int *coins = new unsigned int(n);
	bool* collection = new bool(n);

	for (unsigned int i = 0; i < n; i++) {
		std::cin >> coins[i];
		int tmp;
		std::cin >> tmp;
		if (tmp > 0)
			collection[i] = true;
		else
			collection[i] = false;
	}
	int max_new_coins = 0;
	unsigned int max_value = 0;

	for (int i = k - 1; i > 0; i--) {
		int new_coins = 0;
		bool* change = calc_change(i, k, coins, n);
		for (unsigned int j = 0; j < n; j++) {
			if (change[j] && !collection[j])
				new_coins++;
		}
		if (new_coins > max_new_coins) {
			max_new_coins = new_coins;
			max_value = i;
		}
	}
	std::cout << max_new_coins << std::endl << max_value;
	return(0);
}

bool* calc_change(unsigned int value, unsigned int k, unsigned int* coins, unsigned int n) {
	bool* ans = new bool(n);
	unsigned int change = k - value;
	for (int i = n - 1; i >= 0; i--) {
		if (coins[i] <= change) {
			ans[i] = true;
			change = change % coins[i];
		}
		else
			ans[i] = false;
	}
	return ans;
}