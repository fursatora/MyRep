$(document).ready(function() {
    $("#id_subject").change(function() {
        var subjectId = $(this).val();

        $.ajax({
            url: '/get_teachers/',
            data: {
                'subject_id': subjectId
            },
            dataType: 'json',
            success: function(data) {
                $("#id_workers").html("");  // Очищаем список преподавателей

                // Добавляем отфильтрованных преподавателей в select
                $.each(data, function(index, workers) {
                    $("#id_workers").append(
                        $("<option></option>")
                            .attr("value", workers.id)
                            .text(workers.firstname + " " + workers.lastname)
                    );
                });
            }
        });
    });
});