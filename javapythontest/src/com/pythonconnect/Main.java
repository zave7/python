package com.pythonconnect;

public class Main {

    private static void print(BuildingType building) {
        System.out.println("Building Info: " +
                building.getBuildingId() + " " +
                building.getBuildingName() + " " +
                building.getBuildingAddress());
    }

    /**
     * 팩토리의 create() 메소드를 호출함으로써 세 개의 건물 개체를
     * 생성.
     */

    public static void main(String[] args) {
        BuildingFactory factory = new BuildingFactory();
        print(factory.create("BUILDING-A", "100 WEST MAIN", "1"));
        print(factory.create("BUILDING-B", "110 WEST MAIN", "2"));
        print(factory.create("BUILDING-C", "120 WEST MAIN", "3"));

    }

}