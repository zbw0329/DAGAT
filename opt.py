import argparse
parser = argparse.ArgumentParser(description='train', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--name', type=str, default='dblp')
parser.add_argument('--k', type=int, default=3)
parser.add_argument('--lr', type=float, default=1e-3)
parser.add_argument('--n_clusters', default=4, type=int)
parser.add_argument('--n_z', default=10, type=int)
parser.add_argument('--pretrain_path', type=str, default='pkl')
parser.add_argument('--seed', type=int, default=2)
parser.add_argument('--seed_dblp', type=int, default=14)
parser.add_argument('--seed_usps', type=int, default=5)
parser.add_argument('--seed_cite', type=int, default=4)
parser.add_argument('--seed_acm', type=int, default=10)
parser.add_argument('--seed_hhar', type=int, default=11)
parser.add_argument('--seed_reut', type=int, default=18)
parser.add_argument('--lambda_v1', type=float, default=0.1)
parser.add_argument('--lambda_v2', type=float, default=0.01)
parser.add_argument('--device', type=str, default='cuda')
args = parser.parse_args()