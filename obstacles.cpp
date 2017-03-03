#include <iostream>
#include <cstdlib>
using namespace std;

//void qsort( void* ptr, size_t count, size_t size, int (*comp)(const void *, const void *));
int obstacles[100001][2];
int comp(const void * a, const void * b)
{
    const int *c1=(const int*)a;
    const int *c2=(const int*)b;
    return c1[0]-c2[0];
}
int main()
{
    int test, no_rows, no_obstacles,i,j,k,maxR,x,y;
    int que[3]={0}, new_que[3];
    new_que[0]=new_que[1]=new_que[2]=1;
    cin >> test;
    for(;test;test--)
    {
        cin>>no_rows;
        cin>>no_obstacles;
        for(i=0;i<no_obstacles;i++)
        {
            cin>>x>>y;
            obstacles[i][0]=x;
            obstacles[i][1]=y;
        }
        qsort(obstacles, no_obstacles, sizeof(*obstacles), comp);
        for(i=0,k=0;i<no_rows && k<no_obstacles;k++)
        {
            if(obstacles[k][0]>i)
            {
                //copy new_que to que
                for(j=0;j<3;j++)
                {
                    if(new_que[j]!=-1)
                        que[j]=1;
                    else
                        que[j]=0;
                    new_que[j]=0;
                }
                if(que[0]==1 || que[1]==1)
                    new_que[0]=1;
                else
                    new_que[0]=-1;
                if(que[0]==1 || que[1]==1 || que[2]==1)
                    new_que[1]=1;
                else
                    new_que[1]=-1;
                if(que[1]==1 || que[2]==1)
                    new_que[2]=1;
                else
                    new_que[2]=-1;
                //no position in new row is reachable
                if(!new_que[0] && !new_que[1] && !new_que[2])
                    break;
                i++;
            }
            if(obstacles[k][0]==i)
            {
                new_que[obstacles[k][1]]=-1;
            }
        }

        if(k<no_obstacles)
            maxR=i;
        else
            maxR=no_rows-1;
        cout<<maxR;

    }
}
