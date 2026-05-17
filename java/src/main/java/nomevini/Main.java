package nomevini;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

    }

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[0];
        for (int i=0; i < nums.length; i++){
            for (int y=i + 1; y < nums.length - 1; y++){
                if (i + y == target){
                    result[0] = i;
                    result[1] = y;
                }

            }
        }
        return result;
    }
}