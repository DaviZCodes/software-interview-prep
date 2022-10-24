/*
File: Creating a Company - Fire and Hire Workers
Author: DaviZCodes
Description: This program will create an Employee class, where the employee
 can either be a boss or a worker. The employee will be able to hire and fire people.
 If hired, the person's boss is then the employee and the employee will have the person in their team.

 This uses data hiding, output operator, and pointers.

 NOTE: A can hire B while B hires C and C hires A. There is no logical hierarchy in this system.
 */


#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

class Employee{
    friend ostream& operator<<(ostream& os, const Employee& anEmployee){
        os << anEmployee.name << " is " << anEmployee.age << " years old." << endl;
        //if employee is unemployed
        if (anEmployee.boss == nullptr && anEmployee.team.size() == 0){
            os << anEmployee.name << " is unemployed. ";
            os << endl;
            return os;
        }
        //if employee is a boss
        if (anEmployee.boss == nullptr || anEmployee.team.size() != 0){
            os << anEmployee.name << " is the boss and his team consists of: ";
            //output for the team
            if (anEmployee.team.size() == 0){
                os << "nobody" << endl;
                return os;
            }
            for (size_t i = 0; i < anEmployee.team.size(); ++i){
                os << anEmployee.team[i]->name << " ";
            }
            os << endl;
            return os;
        }
        os << anEmployee.name << "'s boss is " << anEmployee.boss->name;
        if (anEmployee.team.size() == 0){
            os << " and nobody is on his/her team." << endl;
            return os;
        }
        for (size_t i = 0; i < anEmployee.team.size(); ++i){
            os << ". But he/she has a team consisting of: ";
            os << anEmployee.team[i]->name << " ";
        }
        os << endl;
        return os;
    }
public:
    //constructor
    Employee(const string& name, int age, Employee* boss = nullptr) :
    name(name), age(age), boss(boss) {
        if (boss != nullptr){
            boss->team.push_back(this);
        }
        if (age < 0){
            cerr << name << "'s age cannot be lower than 0" << endl;
        }
    }

    bool hire(Employee& anEmployee){
        //checking for false statements
        if (this == &anEmployee || anEmployee.boss != nullptr || boss == &anEmployee){
            cerr << name << " could not hire " << anEmployee.name;
            return false;
        }
        anEmployee.boss = this;
        team.push_back(&anEmployee);
        return true;
    }

    bool fire(Employee& anEmployee){
        for (size_t i = 0; i < team.size(); ++i){
            if (team[i] == &anEmployee){
                // if order does not matter
                team[i] = team[team.size() - 1];
                team.pop_back();
                anEmployee.boss = nullptr;
                return true;

                /* if order does matter
                while (i + 1 < team.size()){
                    team[i] = team[i+1];
                }
                team.pop_back();
                anEmployee.boss = nullptr;
                return true;
                */
            }
        }
        return false;
    }

private:
    string name;
    int age;
    Employee* boss;
    vector<Employee*> team;

};

int main() {
    Employee fredley("Fredley", 28);
    Employee bezos("Bezos", 60);
    Employee jeffrey("Jeffrey", 30, &bezos);
    Employee bezosassistant("Sophie", 18, &bezos);
    Employee bezoshelper("Efrosp", 31313, &bezos);
    Employee wanna_be_fired("Bad Worker", 1, &bezos);
    Employee potato("potato", 0);

    //creating negative age WHICH WILL RESULT IN ERROR MESSAGE
    Employee inexistent("floating in space", -1);

    cout << fredley;
    cout << bezos;
    cout << jeffrey;
    cout << bezosassistant;
    cout << bezoshelper << "And Efrosp is immortal!";
    cout << wanna_be_fired;
    cout << endl;
    cout << potato;

    cout << endl;

    cout << "Now Bad Worker is fired by Bezos because they are a bad worker." << endl;
    bezos.fire(wanna_be_fired);
    cout << wanna_be_fired;
}
