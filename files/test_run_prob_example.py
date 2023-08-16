import run_prob_example

def test_sum_ab():
    output = run_prob_example.sum_ab(1, 6)
    assert isinstance(output, int), 'ERROR: Not float'


if __name__ == '__main__':
  test_sum_ab()