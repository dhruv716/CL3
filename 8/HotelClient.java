import java.rmi.*;
import java.util.*;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelServiceInterface hotelService = (HotelServiceInterface) Naming.lookup("rmi://localhost/HotelService");
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("1. Book a room");
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
                        if (booked) {
                            System.out.println("Room booked successfully!");
                        } else {
                            System.out.println("Room booking failed.");
                        }
                        break;

                    case 2:
                        System.out.print("Enter guest name to cancel: ");
                        String cancelGuest = scanner.nextLine();
                        boolean canceled = hotelService.cancelBooking(cancelGuest);
                        if (canceled) {
                            System.out.println("Booking canceled successfully!");
                        } else {
                            System.out.println("Cancellation failed.");
                        }
                        break;

                    case 3:
                        Map<Integer, String> bookedRooms = hotelService.showBookedRoomDetails();
                        if (bookedRooms.isEmpty()) {
                            System.out.println("No rooms are booked currently.");
                        } else {
                            System.out.println("Room No. | Guest Name");
                            for (Map.Entry<Integer, String> entry : bookedRooms.entrySet()) {
                                System.out.println(entry.getKey() + "       | " + entry.getValue());
                            }
                        }
                        break;

                    case 4:
                        System.out.println("Exiting...");
                        System.exit(0);
                        break;

                    default:
                        System.out.println("Invalid choice.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
