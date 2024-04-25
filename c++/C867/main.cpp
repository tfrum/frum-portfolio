#include "degree.h"
#include "student.h"
#include "roster.h"

#include <string>
#include <iostream>
#include <array>
#include <sstream>

int main() {

    // print out my student information
    std::cout << "Course Title: C867" << std::endl;
    std::cout << "Programming language: C++" << std::endl;
    std::cout << "Student ID: " << std::endl;
    std::cout << "Student Name: " << std::endl;
    std::cout << std::endl;

    // our provided input data
    const std::string studentData[] = 
    {"A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
     "A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
     "A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
     "A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
     "A5,T,Frum,tfrum@wgu.edu,99,2,3,1,SOFTWARE"};

    // create our roster object
    Roster roster;

    // pipe data into the roster
    for (const std::string& data : studentData) {
        roster.parseAndAddStudent(data);
    }


    /* TESTING OUR FUNCTIONS AND CODE*/
    // do we have all of our students?
    roster.printAll();
    std::cout << std::endl;

    // print by invalid email
    roster.printInvalidEmails();

    // print out average days in course for each student

    Student** classRosterArray = roster.getClassRosterArray();
    for (int i = 0; i < 5; ++i) {
        std::string studentID = classRosterArray[i]->getStudentID();
        roster.printAverageDaysInCourse(studentID);
    }

    // print by degree program
    roster.printByDegreeProgram(DegreeProgram::SOFTWARE);

    // remove a student
    roster.remove("A3");
    std::cout << std::endl;

    roster.printAll();
    std::cout << std::endl;

    roster.remove("A3");

    std::cout << std::endl;

    return 0;
}



