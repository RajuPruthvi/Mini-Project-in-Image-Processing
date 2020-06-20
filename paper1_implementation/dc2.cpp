#include<bits/stdc++.h>
using namespace std;

#define watch(x) cerr << (#x) << " is " << x << "\n";

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
    os << "[";
    typename vector< T > :: const_iterator it;
    for( it = v.begin(); it != v.end(); it++ ) {
        if( it != v.begin() ) os << ", ";
        os << *it;
    }
    return os << "]";
}

double pi = acos(-1);

const int M = 161, N = 165;


double a[M+2][N+2], b[M+2][N+2], c[M+2][N+2];
vector<double> ch, cw;

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // Your code here
    double tmpm = 1.0/sqrt(M);
    double tmpn = 1.0/sqrt(N);
    ch = vector<double>(M+2, 2*tmpm);
    cw = vector<double>(N+2, 2*tmpn);
    ch[1] = tmpm;
    cw[1] = tmpn;
    for(int i=1; i<=M; i++) {
        for(int j=1; j<=N; j++) {
            cin>>a[i][j];
        }
    }
    for(int h=1; h<=M; h++) {
        for(int w=1; w<=N; w++) {
            double sum = 0;
            double a1 = h/322.0, a2 = w/330.0;
            for(int i=1; i<=M; i++) {
                for(int j=1; j<=N; j++) {
                    sum += a[i][j]*cos(pi*(2*i+1)*a1)*cos(pi*(2*j+1)*a2);
                }
            }
            b[h][w] = ch[h]*cw[w]*sum;
            // cout << b[h][w] << "\n";
        }
        // cout << "\n";
    }
    // cout << "\n\n\n\n\n";

    for(int h=1; h<=M; h++) {
        for(int w=1; w<=N; w++) {
            double sum = 0;
            double a1 = pi*(2*h+1)/322.0, a2 = pi*(2*w+1)/330.0;
            for(int i=1; i<=M; i++) {
                for(int j=1; j<=N; j++) {
                    sum += ch[i]*ch[j]*b[i][j]*cos(i*a1)*cos(j*a2);
                }
            }
            c[h][w] =sum;
            int tmp = c[h][w];
            if(tmp < 0) tmp = 0;
            if(tmp > 255) tmp = 255;
            cout << tmp << "\n";
        }
        // cout << "\n";
    }
    // cout << "\n";
    return 0;
}

