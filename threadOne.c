#include <pthread.h>
#include <stdio.h>

void* fun(void *arg){
	int x;
	for (x=0; x<100; ++x)
		printf("X");

	return arg;
}

int main(){
	int x;
	pthread_t tid;
	pthread_create(&tid, NULL, fun, NULL);
	for (x=0; x<100; ++x)
		printf("O");

	//pthread_join(tid,NULL);
}

