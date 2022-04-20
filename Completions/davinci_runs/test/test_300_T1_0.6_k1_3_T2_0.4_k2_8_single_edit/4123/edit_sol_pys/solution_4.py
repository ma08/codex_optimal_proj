import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class File {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO 自動生成されたメソッド・スタブ
		File file = new File("sample.txt");
		Scanner scan = new Scanner(file);
		while(scan.hasNext()){
			String str = scan.next();
			System.out.println(str);
		}
		scan.close();
	}

}
