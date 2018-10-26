#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#define MAX   (~(0x1<<31))

using namespace std;

string str;

vector<vector<int> > adjaceny_matrix;
vector<int> outputE_copy;
vector<int> outputV;
vector<int> path;
vector<int> outputS;


int start,stop,n;


void vsplit()
{
    outputV.clear();
    outputE_copy.clear();

    std::vector<std::string> a;
     std::size_t prev_pos = 0, pos;
         while ((pos = str.find_first_of(" ", prev_pos)) != std::string::npos)
         {
            if (pos > prev_pos)
              a.push_back(str.substr(prev_pos, pos-prev_pos));
            prev_pos= pos+1;
         }
        if (prev_pos< str.length())
            a.push_back(str.substr(prev_pos, std::string::npos));





for (auto &s : a) {
    std::stringstream parser(s);
    int x = 0;

    parser >> x;

    outputV.push_back(x);
}
n=outputV[1];

}
void init_adjacency_matrix()

  {
     int gv_num = outputV[1];
    adjaceny_matrix.resize(gv_num);
    for (auto &i:adjaceny_matrix)
    {
        i.resize(gv_num,MAX);
    }
  }
void adjacency_matrix(int u,int v)
{

    adjaceny_matrix[u][v]=1;
    adjaceny_matrix[v][u]=1;
}



void Source_Dest()
{
    init_adjacency_matrix();

    int u,v;
    for(int j=1; j<outputE_copy.size(); j=j+2)
       {
           u=outputE_copy[j-1];
           v=outputE_copy[j];
          // cout<<"u is"<<u<<endl;
           //cout<<"v is"<<v<<endl;
           adjacency_matrix(u,v);


       }
}
void Esplit()
{

    vector<string> b;
     std::size_t prev_pos = 0, pos;
         while ((pos = str.find_first_of("{<,>}", prev_pos)) != std::string::npos)
         {
            if (pos > prev_pos)
              b.push_back(str.substr(prev_pos, pos-prev_pos));
            prev_pos= pos+1;
         }
        if (prev_pos< str.length())
            b.push_back(str.substr(prev_pos, std::string::npos));
    vector<int> outputE;



    for (auto &s : b) {

        std::stringstream parser(s);
        int x = 0;

        parser >> x;

    outputE.push_back(x);
}

int check=0;
   for (int i=1; i<outputE.size(); i++)
   {
        if(outputE[i]>=0 && outputE[i]<n)
        {
            outputE_copy.push_back(outputE[i]);
        }
       else{
        check=1;
       }
   }

if(check==1)
{
    cout<<"Error: Edges out of range"<<endl;
}

 Source_Dest();
}

void Ssplit()
{

 outputS.clear();

    vector<string> c;
     std::size_t prev_pos = 0, pos;

         while ((pos = str.find_first_of(" ", prev_pos)) != std::string::npos)
         {
            if (pos > prev_pos)
              c.push_back(str.substr(prev_pos, pos-prev_pos));
            prev_pos= pos+1;
         }
        if (prev_pos< str.length())
            c.push_back(str.substr(prev_pos, std::string::npos));
     vector<int> outputS;

    for (auto &s : c) {
        std::stringstream parser(s);
        int x = 0;

        parser >> x;

    outputS.push_back(x);
}
start=outputS[1];
stop=outputS[2];

}

void shortest_path(int Source,int Destination) {
//cout<<"source"<<Source<<endl;
//cout<<"destination is"<<Destination<<endl;
//cout<<"value of n is:"<<n<<endl;
    if (Source >= n|| Destination >=n)
    {
        cout<<"Error: Vertex out of range"<<endl;
    }
else{
          unsigned int new_dist;
    unsigned int flag[n];

    unsigned int dist[n];
    path.clear();


    for (unsigned int i = 0; i < n; i++) {
        flag[i] = 0;

        dist[i] = adjaceny_matrix[Source][i];

    }


    flag[Source] = 1;
    dist[Source] = 0;

    for (unsigned int i = 1; i < n; i++) {

        unsigned int min = MAX;
        //cout<<min;
        unsigned int k = 0;
        for (int x = 0; x < n; x++) {
            if (flag[x] == 0 && dist[x] < min) {
                min = dist[x];
                k = x;
            }
        }

        flag[k] = 1;


        for (int j = 0; j < n; j++) {
            new_dist = (adjaceny_matrix[k][j] == MAX ? MAX : (min + adjaceny_matrix[k][j]));
            if (flag[j] == 0 && (new_dist < dist[j])) {
                dist[j] = new_dist;

            }
        }
    }

    if (dist[Destination] == MAX)
    {
        cout<<"Error: No path exists between these vertices."<<endl;
    }

    unsigned int vertex = Destination;
    while (dist[vertex] > 0) {

        path.push_back(vertex);



        for(size_t i = 0; i<n; ++i)
        {
            if(adjaceny_matrix[vertex][i] < MAX &&
               dist[i] + adjaceny_matrix[vertex][i] == dist[vertex])
            {
                vertex = i;
                break;
            }
        }
    }
    path.push_back(vertex);

  for (auto mk = path.rbegin(); mk != path.rend(); mk++)
    {
        std::cout << *mk;
        if (mk != path.rend() - 1) {
                //cout<<"path true"<<endl;
            std::cout << "-";
        } else
        {
            //cout<<"path false"<<endl;
            std::cout << "\n";
        }

    }

}

}


int main()
{

    while(getline(cin,str))

    {

                if(str[0]=='v')
                {
                    vsplit();

                }
                else if(str[0]=='e')
                {

                    Esplit();

                }
                else if(str[0]=='s')
                {

                    Ssplit();
                    shortest_path(start,stop);
                }

}

    return 0;
}

