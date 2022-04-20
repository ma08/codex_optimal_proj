import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class file {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("/Users/user/IdeaProjects/lab1/src/main/resources/file.txt");

        Scanner sc = new Scanner(file);
        String str = sc.nextLine();
        String[] arr = str.split(" ");
        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}
