public class factorial {
    //A simple code to execute factorial of any number;
    public static int fact(int k){
        if(k == 1){
            return 1;
        }else{
            return (k*fact(k-1));
        }
    }

    public static void main(String[] args) {
        int result = fact(4);
        System.out.println(result);
    }
    
}
