#include <stdio.h>
#include <stdlib.h>
struct player {
	int play_id;
	char name[50];
};

struct sports {
	void (*run)();
	void (*game)();
	void (*socker)();
	char notes[12];
};
struct sports *sp;
struct player *play;

void getshell()
{
	system("/bin/sh");
}


int main()
{
	sp = (struct sports*)malloc(sizeof(sp));
	free(sp);
	printf("%d",sizeof(sp));
	play = (struct player*)malloc(sizeof(play));
	play -> play_id = getshell;
	sp -> run();

}
