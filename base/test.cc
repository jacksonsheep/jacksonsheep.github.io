# include <iostream>
# include <vector>
# include <map>
using namespace std;

int main(){
  vector<int> list;
  map<int, string> name;
  list.emplace_back(1);
  for (int i = 0; i < list.size(); i++){
      cout << list[i] << endl;
  }
  cout << "hello world" << endl;
  return 0;
}