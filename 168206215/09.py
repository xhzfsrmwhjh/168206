#include <iostream>
#include <vector>
using namespace std;

int main()
{
    for (int x=1;x<4;++x)
    {
        if (1 == (x != 1) + (x == 4) + (x == 2) + (x != 4))
        {
            cout<<char(x-1+'A')<<"是小偷"<<endl;
        }
    }
    return 0;
}
