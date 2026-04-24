#include <iostream>
#include <string>

class song{
    private:
        std::string title;
        std::string artist;
        float duration;
        int playCount;
    
    public:
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

int main(){
    song song1("Bulleya", "Papon", 357);
    song song2("Sach keh raha hai", "KK", 329);

    song1.display();
    song2.display();
    song1.play();
    
    std::cout<<"Play Count: "<< song1.getPlayCount()<<std::endl;
    std::cout<<"Play Count: "<< song2.getPlayCount()<<std::endl;

}