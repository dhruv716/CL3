import java.rmi.*;
import java.util.*;

public interface HotelServiceInterface extends Remote {
    boolean bookRoom(String guestName, int roomNumber) throws RemoteException;
    boolean cancelBooking(String guestName) throws RemoteException;
    Map<Integer, String> showBookedRoomDetails() throws RemoteException;
}
