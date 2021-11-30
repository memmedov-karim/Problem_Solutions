#include<stdio.h>
int main(){
	int n,say=0;
	scanf("%d",&n);
	n--;
	say=say+4;
	if(n>0){
		n--;
		say=say+3;
	}
	int count=2,score=0;
	while(n>0){
		if(score==2){
			score=0;
			count++;
		}
		n-=count;
		say+=3+(count-1)*2;
		score++;
	}
	if(n<0){
		say+=n*2;
	}
	printf("%d",say);
	return 0;
}
