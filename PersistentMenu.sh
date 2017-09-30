curl -X POST -H "Content-Type: application/json" -d '{
  "persistent_menu":[
    {
      "locale":"default",
      "composer_input_disabled":false,
      "call_to_actions":[
        {
          "type":"postback",
          "title":"SMART HOME",
          "payload":"USER_DEFINED_PAYLOAD_HOME"
        },
        {
          "type":"postback",
          "title":"ABOUT",
          "payload":"USER_DEFINED_PAYLOAD_ABOUT"
        }
      ]
    }
  ]
}' "https://graph.facebook.com/v2.10/me/messenger_profile?access_token=xxxxxxxxxxxxxxxxxxxxxxxxx"