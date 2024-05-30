function toggleSelection(event) {
  event.preventDefault();
  var target = event.currentTarget;

  if (target.classList.contains("selected")) {
    target.classList.remove("selected");
  } else {
    target.classList.add("selected");
  }
  event.stopPropagation();
}
function rolechangeTemplate(event){
  if(event.target.value==='OnlyAgent'){
    $('#password').hide()
  }else{
    $('#password').show()
  }

}
  //SERILIZE AGENTS DATA 
  function serializer(AgentTemplate) {
    const agentData = {
      first_name: AgentTemplate.find('span[name="firstname"]').text(),
      last_name: AgentTemplate.find('span[name="lastname"]').text(),
      password:AgentTemplate.find('input[name="password"]').val(),
      role: AgentTemplate.find('select[name="role"]').val(),
      country: AgentTemplate.find('span[name="country"]').text(),
      age: AgentTemplate.find('span[name="age"]').text(),
      balance: AgentTemplate.find('span[name="balance"]').text(),
    };
    return agentData
  }

//DELETE AGENT FROM DASHBOARD
function deleteAgent(id) {
  $.ajax({
    url: "/home/delete-agent/",
    type: "DELETE",
    dataType: "json",
    data: JSON.stringify({ 'data': id }),
    headers: {
      "X-CSRFToken": csrf_token,
    },
    success: function (response) {
      console.log(response)
      $("#AgentContainer" + id).remove()
    },
    error: function (error) {
      console.log(error)
      console.error("Error sending agent data:", error);
    },
  });
}
//EIDIT AGENT FROM DASHBOARD
function editAgent(event,id) {
  event.preventDefault();
  const agent = $("#AgentContainer" + id)
  const target=$(event.target)
  if(target.hasClass("selected")){
    target.removeClass("selected")
    agent.removeClass("selected")
    target.text('Edit')
    data =serializer(agent)
    data['id']=id
    $.ajax({
      url: "/home/update-agent/",
      type: "PUT",
      dataType: "json",
      data: JSON.stringify({'data':data}),
      headers: {
        "X-CSRFToken": csrf_token,
      },
      success: function (response) {
        console.log(response)
        // $("#AgentContainer"+id).remove()
      },
      error: function (error) {
        console.log(error)
        console.error("Error sending agent data:", error);
      },
    });

  }
else{
  target.addClass("selected")
  agent.addClass("selected")
  target.text('Save')
}
}

const newAgentHolder = `
<div id="createdAgentTemplate" class="col mb-5 selected">
<div class="card h-100">
    <!--  image-->
    <select onchange="rolechangeTemplate(event)" name="role" class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem" >
    <option value="Admin">Admin</option>
    <option value="Support">Support</option>
    <option value="Developer">Developer</option>
    <option value="OnlyAgent" selected>OnlyAgent</option>
  </select>
    <img class="card-img-top" src=${imagePath} alt="..." width="450" 
    height="200"  />
    <!--  details-->
    <div class="card-body p-4">
        <div class="text-center">
        <span class="fw-bolder" name="id"></span>
        <span  class="fw-bolder" name="firstname" contentEditable="true" data-placeholder="First Name"></span>
        <span  class="fw-bolder" name="lastname" contentEditable="true" data-placeholder="Last Name"></span>
        <span class="fw-bolder" name="country" contentEditable="true" data-placeholder="Country"></span>
        <hr/>
        <input style="display:none" name="password" id="password" type="password" placeholder="User password...."/>
        <hr/>
        <strong><span  name="age" contentEditable="true" data-placeholder="Age"></span><span class="age"> Years</span></strong>
        <br/>
        <span>$</span>
        <span  name="balance" contentEditable="true" data-placeholder="$80.00"></span>
        </div>
    </div>
    <!-- Prouct actions-->
    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent" style="display:flex;justify-content: space-between;">
        <div class="text-center"><button id="addAgent" class="btn btn-outline-dark mt-auto selected">Save</button></div>
        <div class="text-center"><button id="deleteAgent" class="btn btn-outline-dark mt-auto">Discard</button></div>
    </div>
</div>
</div>`;

$(document).ready(function () {
  var isAgentAdded = false;
  var originalContainer = $("#AgentsContainers");


  //ADD NEW AGENT TEMPLATE
  $("#addContainerBtn").on("click", function () {
    if (isAgentAdded) return;
    $('#emptybox').remove()
    originalContainer.append(newAgentHolder);
    isAgentAdded = true;

  })


  //SAVE NEW AGENT TEMPLATE
  $(document).on("click", "#addAgent, #deleteAgent", function (event) {
    event.preventDefault();
    var target = $(event.currentTarget);
    var agentCard = target.closest(".col.mb-5");
    if (target.attr("id") === "addAgent") {
      sendAgentData(agentCard, target);
    } else if (target.attr("id") === "deleteAgent") {
      agentCard.remove();
      isAgentAdded = false;
    }
  });



  //Extract DATE FROM NEW AGENT TEMPLATE
  function sendAgentData(agentCard, addButton) {
    let agentData = serializer(agentCard)
    $.ajax({
      url: "/home/create-agent/",
      type: "POST",
      dataType: "json",
      data: JSON.stringify({ 'data': agentData }),
      headers: {
        "X-CSRFToken": csrf_token,
      },
      success: function (response) {
        agentCard.attr('id','AgentContainer' + response.ID)
        agentCard.removeClass("selected")
        agentCard.find("span[name='id']").text('ID:' + response.ID);
        agentCard.find("button [id='deleteAgent']").on('click', (event,id = response.ID) => deleteAgent(id))
        agentCard.find('input[name="password"]').remove()
        addButton.text('Edit')
        addButton.removeClass('selected')


        $(document).off("click", "#addAgent, #deleteAgent");

        addButton.on('click', function(event,id=response.ID) {
          editAgent(event,id)
        });
        addButton.removeAttr('id')

        const deleteButton=$('#deleteAgent')

        deleteButton.on('click',(event,id=response.ID)=> deleteAgent(id))
        deleteButton.removeAttr('id')
        console.log(role)
        if(role !='Admin'){
          console.log("inside the conditoon")
          agentCard.find('[contentEditable="true"]').removeAttr('contentEditable').removeClass('fw-bolder');
          console.log(agentCard.find('select [name="role"]'))
          agentCard.find('select[name="role"]').replaceWith(`<span name="role" class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem">
          ${agentCard.find('select [name="role"]').val()}
          </span>`)
          deleteButton.remove()
          addButton.remove()

        }
        isAgentAdded = false;
      },
      error: function (error) {
        console.error("Error sending agent data:", error);
      },
    });
  }


















  // JavaScript to handle the focus event and select all text
  $(document).ready(function () {
    // Function to select all text inside contentEditable on focus
    function selectAllText(contentEditableElement) {
      var range = document.createRange();
      range.selectNodeContents(contentEditableElement);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    }

    // Attach the event to all contentEditable elements
    $(document).on('focus', '[contentEditable=true]', function () {
      selectAllText(this);
    });

    // Placeholder effect for contentEditable
    $('[contentEditable=true]').on('blur', function () {
      var element = $(this);
      if (!element.text().trim().length) {
        element.empty();
      }
    });
  });

});
