#include <iostream>
#include <string>

class song{
    private:
        std::string title;
        std::string artist;
        float duration;
        int playCount;
    
    public:
        song(){}
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
        playlist(){}
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
class user{
    private:
        std::string username;
        playlist playlists[5];
        int playlistCount;
    
    public:
        user(std::string username){
            this -> username = username;
            playlistCount = 0;
        }
        void addPlaylist(playlist &obj){
            if(playlistCount < 2){
                playlists[playlistCount] = obj;
                playlistCount++;
            }
            else{
                std::cout<<"MAX playlist limit reached!"<<std::endl;
            }
        }
        void createPlaylist(std::string playlistName){
            playlist playlist(playlistName);
            addPlaylist(playlist);
            std::cout<<"Playlist Created!"<<std::endl;
        }

        void display(){
            std::cout <<"*****"<<username<<"*****"<<std::endl;
            for (int i = 0; i != playlistCount; i++){
                playlists[i].display();
            }
        }
};
int main(){
    song song1("Bulleya", "Papon", 357);
    song song2("Sach keh raha hai", "KK", 329);

    user user1("Amish");
    user1.createPlaylist("3 AM Songs");
    user1.createPlaylist("PHONK");
    user1.createPlaylist("AIZEN");

}
