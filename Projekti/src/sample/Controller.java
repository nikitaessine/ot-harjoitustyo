package sample;

import java.awt.event.ActionEvent;
import java.awt.event.MouseEvent;
import java.beans.EventHandler;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import java.util.ArrayList;

public class Controller {

    ArrayList<String> tasks;

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private TextField main_field;

    @FXML
    private Button add_btn;

    @FXML
    private VBox all_tasks;

    @FXML
    void initialize() {



        add_btn.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {


            public void handler(MouseEvent mouseEvent) {

                if (!main_field.getText().trim().equals("")) {
                    tasks.add(main_field.getText());
                    addTask();
                    main_field.setText("");
                }

            }

        });

        addTask();
    }

    private void addTask(){

        all_tasks.getChildren().clear();

        for (int i = 0; i<tasks.size(); i++){
            all_tasks.getChildren().add(new Label(tasks.get(i)));
        }



    }


}

