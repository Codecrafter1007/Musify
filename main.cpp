#include <iostream>
#include <string>

class song{
    private:
        std::string title;
        std::string artist;
        float duration;
        int playCount;
    
    public:
        song(){
        }
        song(std::string title,std::string artist, float duration){
            this -> title = title;
            this -> artist = artist;
            this -> duration = duration;
            playCount = 0;
        }
    
        void display(){
            std::cout <<title<<" by "<<artist<<std::endl;
        }
        
        void play(){
            playCount++;
            std::cout << "Now Playing ";
            display();
        }

        int getPlayCount(){
            return playCount;
        }
};
class playlist{
    private:
        std::string playListName;
        song songs[10];
        int songCount;
    
    public:
        playlist(std::string playListName){
            this -> playListName = playListName;
            songCount = 0;
        }

        void addSong(song &obj){
            if(songCount < 10){
                songs[songCount] = obj;
                songCount++;
                std::cout <<"Song added!"<<std::endl;
            }
            else{
                std::cout<<"MAX song limit reached!"<<std::endl;
            }
        }

        void display(){
            std::cout<<"-------------"<<playListName<<"-------------"<<std::endl;
            
            for (int i = 0; i != songCount; i++){
                songs[i].display();
            }
            
        }
};
int main(){
    song song1("Bulleya", "Papon", 357);
    song song2("Sach keh raha hai", "KK", 329);

    playlist playlist1("3AM Songs");

    playlist1.addSong(song1);
    playlist1.addSong(song2);

    playlist1.display();
    std::cout<<song1.getPlayCount()<<std::endl;
    std::cout<<song2.getPlayCount()<<std::endl;
}