package Week1;

import java.util.Arrays;

public class WeightedQuickUnionUF {
	
	private int[] id;
	private int[] sz;
	private int[] gv;
	
	public WeightedQuickUnionUF(int N) {
		id = new int[N];
		sz = new int[N]; // size of tree
		gv = new int[N]; // greatest value in tree
		for (int i = 0; i < N; i++) {
			id[i] = i;
			sz[i] = 1;
			gv[i] = i;
		}
	}
	
	private int root(int i) {
		while (id[i] != i) {
			// with path compression:
			id[i] = id[id[i]];
			i = id[i];
		}
		return i;
	}
	
	public boolean connected(int p, int q) {
		return root(p) == root(q);
	}
	
	public void union(int p, int q) {
		int small = p;
		int large = q;
		if (sz[p] > sz[q]) {
			small = q;
			large = p;
		}
		gv[root(large)] = Math.max(gv[root(small)], gv[root(large)]);
		id[root(small)] = root(large);
		sz[large] += sz[small];
	}
	
	public int find(int i) {
		return gv[root(i)];
	}
	
	public String toString() {
		return Arrays.toString(id) + "\n" + Arrays.toString(sz) + "\n" + Arrays.toString(gv);
	}
	
	public static void main(String[] args) {
		
		WeightedQuickUnionUF uf = new WeightedQuickUnionUF(10);
		uf.union(4,3);
		uf.union(3,8);
		uf.union(6,5);
		uf.union(9,4);
		uf.union(2,1);
		uf.union(8,9);
		uf.union(5,0);
		uf.union(7,2);
		uf.union(6,1);
		uf.union(1,0);
		uf.union(6,7);
		
		System.out.println(uf.toString());
		for (int i = 0; i < 10; i++) {
			System.out.println(uf.find(i));
		}
		
	}
	
}

