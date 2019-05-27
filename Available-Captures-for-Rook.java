/**
On an 8 x 8 chessboard, there is one white rook.  There also may be empty
squares, white bishops, and black pawns.  These are given as characters
'R', '.', 'B', and 'p' respectively. Uppercase characters represent white
pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal
directions (north, east, west, and south), then moves in that direction
until it chooses to stop, reaches the edge of the board, or captures an
opposite colored pawn by moving to the same square it occupies.  Also,
rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
**/

class Solution {
    public int numRookCaptures(char[][] board) {
        int count = 0;
        // find the location of the rook currently
        int rook_x = 0;
        int rook_y = 0;
        boolean found = false;
        for(int i=0; i<board.length; i++) {
            for(int j=0; j<board[0].length; j++) {
                if(board[i][j] == 'R') {
                    rook_x = i;
                    rook_y = j;
                    found = true;
                    break;
                }
                if(found)
                    break;
            }
        }

        //Move downward
        for(int i=rook_y; i<board.length; i++) {
            char c = board[rook_x][i];
            if(c == 'B') break;
            if(c == 'p') {
                count++;
                break;
            }
        }

        //Move leftward
        for(int i=rook_x; i>=0; i--) {
            char c = board[i][rook_y];
            if(c == 'B') break;
            if(c == 'p') {
                count++;
                break;
            }
        }

        //Move rightward
        for(int i=rook_x; i<board[0].length; i++) {
            char c = board[i][rook_y];
            if(c == 'B') break;
            if(c == 'p') {
                count++;
                break;
            }
        }

        //Move upward
        for(int i=rook_y; i>=0; i--) {
            char c = board[rook_x][i];
            if(c == 'B') break;
            if(c == 'p') {
                count++;
                break;
            }
        }

        return count;


    }
}
