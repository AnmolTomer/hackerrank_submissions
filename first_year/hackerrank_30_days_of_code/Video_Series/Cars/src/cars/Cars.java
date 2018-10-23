/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cars;

/**
 *
 * @author anmol
 */
public class Cars {

    /**
     * @param args the command line arguments
     */
    
        // TODO code application logic here
        // Properties field of the object defined below
        int maxSpeed = 100;
        int minSpeed = 0;
        double weight = 4079;
        boolean isTheCarOn = false;
        char condition = 'A';
        String nameOfCar = "Lucy";
        
        public void printVariables() {
            System.out.println("This is the maxSpeed : "+maxSpeed);
            System.out.println("This is the minSpeed : "+minSpeed);
            System.out.println("This is the weight : "+weight);
            System.out.println("Is the car on ? "+isTheCarOn);
            System.out.println("This is the condition of the car : "+condition);
            System.out.println(nameOfCar);
        }
        // println just prints the stuff in a new line each time it is used.
        // This is the blueprint of the car and can be changed whenever we want by calling methods.
        
        // to define a function first we tell it's scope public, protected, private followed by return type be it void or int etc.
        // after void nameOfTheFunction is typed
        public void wreckCar() {
            condition = 'C';
        }
        public void upgradeSpeed() {
            minSpeed = maxSpeed;
            maxSpeed = maxSpeed+1;
        }
        public static void main(String[] args) {
            //TODO code appplication logic here
            Cars familyCar = new Cars();
            // Creating a new instance from our blue-print or a new object.
            System.out.println("Family's Car");
            familyCar.printVariables();            
            Cars aliceCar = familyCar; //Alice's Car is familyCar
            familyCar.wreckCar();
            System.out.println("Alice's Car");
            aliceCar.printVariables();
            
            familyCar.upgradeSpeed();
            System.out.println("Upgraded Speed");
            familyCar.printVariables();
            // Arrays, Queues, Linkedlists and Stacks are some of the reference types and are types of Data Structures.
            
        }
    
    
}