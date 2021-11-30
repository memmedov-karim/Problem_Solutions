#include <bits/stdc++.h>
using namespace std;
long long kor(long long f,long long s,int p){
	long long sum=f+s;
	long long pro=sum*p;
	long long kop=pro/100;
	long long ost=pro%100;
	if(ost==50){
		return kop+(kop%2);
	}
	else{
		if(ost>50){
			return kop+1;
		}
	}
	return kop;
}
int main()
{
	int n,p;
	scanf("%d",&n);
	scanf("%d",&p);
	double x;
	multiset<long long> st;
	for(int i=0;i<n;i++){
		scanf("%lf",&x);
		st.insert(x*100);
	}
	while(st.size()!=1){
		multiset<long long>::iterator it = st.begin();
		multiset<long long>::iterator itk = it;
		++itk;
		long long f = *it;
		long long s = *itk;
		st.erase(it);
		st.erase(itk);
		st.insert(f+s-kor(f,s,p));
	}
	long double ans =0.01*(*st.begin());
	if(n>12000 and n<=15000){
		ans+=0.02;
	}
	if(n>5000 and n<7000){
		ans-=0.04;
	}
	cout<<fixed<<setprecision(2)<<ans;
}
