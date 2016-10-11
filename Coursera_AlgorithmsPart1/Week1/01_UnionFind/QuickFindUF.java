package Week1;

import java.util.Arrays;

public class QuickFindUF {
	
	private int[] id;
	
	public QuickFindUF(int N) {
		id = new int[N];
		for (int i = 0; i < N; i++) {
			id[i] = i;
		}
	}
	
	public boolean connected(int p, int q) {
		return id[p] == id[q];
	}
	
	public void union(int p, int q) {
		if ( !connected(p, q) ) {
			int pid = id[p];
			int qid = id[q];
			for (int i = 0; i < id.length; i++) {
				if (id[i] == qid) {
					id[i] = pid;
				}
			}
		}
	}
	
	public String toString() {
		return Arrays.toString(id);
	}
	
	public static void main(String[] args) {
		
		QuickFindUF uf = new QuickFindUF(10);
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
	}
	
}