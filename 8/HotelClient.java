import java.rmi.Naming;
import java.util.Map;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelServiceInterface hotelService = (HotelServiceInterface) Naming.lookup("rmi://localhost/HotelService");
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("\n1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. Show booked room details");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // consume newline
                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String guestName = scanner.nextLine();
                        System.out.print("Enter room number: ");
                        int roomNumber = scanner.nextInt();
                        boolean booked = hotelService.bookRoom(guestName, roomNumber);
                        System.out.println(booked ? "Room booked!" : "Booking failed.");
                        break;
                    case 2:
                        System.out.print("Enter guest name: ");
                        String cancelName = scanner.nextLine();
                        boolean cancelled = hotelService.cancelBooking(cancelName);
                        System.out.println(cancelled ? "Booking canceled!" : "Cancellation failed.");
                        break;
                    case 3:
                        Map<Integer, String> bookedRooms = hotelService.showBookedRoomDetails();
                        System.out.println("Room\tGuest");
                        bookedRooms.forEach((room, guest) -> System.out.println(room + "\t" + guest));
                        break;
                    case 4:
                        System.exit(0);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

