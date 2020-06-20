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
int alpha = 1.42867;

double a[M][N], b[M][N], c[M][N];
vector<double> ch, cw;

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // Your code here
    ch = vector<double>(M, sqrt(2/(double)M));
    cw = vector<double>(N, sqrt(2/(double)N));
    ch[0] = sqrt(1/(double)M);
    cw[0] = sqrt(1/(double)N);
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            cin>>a[i][j];
        }
    }
    for(int h=0; h<M; h++) {
        for(int w=0; w<N; w++) {
            double sum = 0;
            double a1 = pi*h/322, a2 = pi*w/330;
            for(int i=0; i<M; i++) {
                for(int j=0; j<N; j++) {
                    sum += a[i][j]*cos((2*i+1)*a1)*cos((2*j+1)*a2);
                }
            }
            b[h][w] = ch[h]*cw[w]*sum;
            // cout << b[h][w] << "\n";
        }
        // cout << "\n";
    }
    // cout << "\n\n\n\n\n";

    for(int h=0; h<M; h++) {
        for(int w=0; w<N; w++) {
            if(abs(b[h][w]) <= 0.01 * b[0][0]) {
                b[h][w] *= alpha;
            }
        }
    }

    for(int h=0; h<M; h++) {
        for(int w=0; w<N; w++) {
            double sum = 0;
            double a1 = pi*(2*h+1)/322, a2 = pi*(2*w+1)/330;
            for(int i=0; i<M; i++) {
                for(int j=0; j<N; j++) {
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

