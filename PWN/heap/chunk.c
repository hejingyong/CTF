#include <stdio.h>
void main() {

	void *p1 = malloc(0x200);
	void *p2 = malloc(0x300);
	strcpy(p1,"chunk1");
	printf("p1 point to  %p\n",p1);
	
	memset(p1,"A",0x208);
	
	printf("see the chunk");
}
/*
0x602000 PREV_INUSE {
pre_size = 0x0,
size = 0x211,
fd = 0x7ffff7dd1b78  <main_arena+88>,
bk = 0x7ffff7dd1b78  <main_arena+88>,
fd_nextsize = 0x1818181818181818,
bk_nextsize = 0x1818181818181818
}

0x602210 PREV_INUSE {
0x602000 PREV_INUSE {
pre_size = 0x210,
size = 0x310,
fd = 0x0,
bk = 0x0,
fd_nextsize = 0x0,
bk_nextsize = 0x0

}

*/
